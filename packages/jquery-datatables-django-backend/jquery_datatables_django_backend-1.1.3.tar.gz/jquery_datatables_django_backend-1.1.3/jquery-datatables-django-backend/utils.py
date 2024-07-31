import urllib.parse

from django.http import JsonResponse


def JqueryDatatable(request, queryset, SerializerClass, columnRemapping=None, additionalColumns=None):
    if request.method == 'DELETE':
        id = urllib.parse.parse_qs(request.body.decode('utf-8')).get('id')[0]
        queryset.get(id=id).delete()
        return JsonResponse({"message": "Deleted Successfully !"})

    requestType = request.GET.get('requestType')
    allColumns = []
    ctr = 0
    columnValue = request.GET.get(f"columns[{ctr}][data]")
    while columnValue:
        try:
            int(columnValue)
        except:
            allColumns.append(columnValue.replace(".", "__"))
        ctr = ctr + 1
        columnValue = request.GET.get(f"columns[{ctr}][data]")

    if additionalColumns and isinstance(additionalColumns, list):
        allColumns = allColumns + additionalColumns

    # For main search
    search = request.GET.get("search[value]")
    if search:
        for eachWord in search.strip().split(" "):
            filteredDataEachWord = queryset.none()
            for eachColumn in allColumns:
                try:
                    if columnRemapping and isinstance(columnRemapping, list):
                        for eachRemapping in columnRemapping:
                            if eachColumn in eachRemapping:
                                if isinstance(eachRemapping[eachColumn], list):
                                    for eachRemappingField in eachRemapping[eachColumn]:
                                        filteredDataEachWord = filteredDataEachWord | queryset.filter(
                                            **{f"{eachRemappingField}__icontains": eachWord})
                                else:
                                    filteredDataEachWord = filteredDataEachWord | queryset.filter(
                                        **{f"{eachRemapping[eachColumn]}__icontains": eachWord})
                                continue
                    filteredDataEachWord |= queryset.filter(**{f"{eachColumn}__icontains": eachWord})
                except:
                    pass
            queryset = queryset & filteredDataEachWord

    # For individual column search
    try:
        for i, column in enumerate(allColumns):
            columnSearchValue = request.GET.get(f"columns[{i}][search][value]").strip() or None
            if not columnSearchValue:
                continue
            lookup = 'icontains'

            if columnSearchValue.lower() == 'yes' or 'paid' in columnSearchValue:
                columnSearchValue = True
            elif columnSearchValue.lower() == 'no' or 'un' in columnSearchValue:
                columnSearchValue = False
            elif columnSearchValue.startswith("=="):
                lookup = 'exact'
                columnSearchValue = columnSearchValue[2:]
            elif columnSearchValue.startswith("="):
                lookup = 'iexact'
                columnSearchValue = columnSearchValue[1:]
            elif columnSearchValue.startswith("<="):
                lookup = 'lte'
                columnSearchValue = columnSearchValue[2:]
            elif columnSearchValue.startswith("<"):
                lookup = 'lt'
                columnSearchValue = columnSearchValue[1:]
            elif columnSearchValue.startswith(">="):
                lookup = 'gte'
                columnSearchValue = columnSearchValue[2:]
            elif columnSearchValue.startswith(">"):
                lookup = 'gt'
                columnSearchValue = columnSearchValue[1:]
            remapFound = False
            if columnRemapping and isinstance(columnRemapping, list):
                for eachRemapping in columnRemapping:
                    if column in eachRemapping:
                        remapFound = True
                        if isinstance(eachRemapping[column], list):
                            fieldsdata = queryset.none()
                            for eachRemappingField in eachRemapping[column]:
                                fieldsdata |= queryset.filter(**{f"{eachRemappingField}__{lookup}": columnSearchValue})
                            queryset = queryset & fieldsdata
                        else:
                            queryset = queryset.filter(**{f"{eachRemapping[column]}__{lookup}": columnSearchValue})
                        break
            if not remapFound:
                queryset = queryset.filter(**{f"{column}__{lookup}": columnSearchValue})
    except:
        pass

    # Data Ordering
    try:
        columnSelected = request.GET.get("order[0][column]" or None)
        columnOrder = request.GET.get("order[0][dir]" or None)
        if columnSelected and columnOrder:
            selectedColumnName = allColumns[int(columnSelected)]
            if columnRemapping and isinstance(columnRemapping, list):
                for eachRemapping in columnRemapping:
                    if selectedColumnName in eachRemapping:
                        if isinstance(eachRemapping[selectedColumnName], list):
                            selectedColumnName = eachRemapping[selectedColumnName][0]
                        else:
                            selectedColumnName = eachRemapping[selectedColumnName]
            if columnOrder == "desc":
                queryset = queryset.order_by(f"-{selectedColumnName}").distinct(selectedColumnName)
            else:
                queryset = queryset.order_by(selectedColumnName).distinct(selectedColumnName)
    except:
        pass

    # Exporting full data if request type is export
    if requestType == 'export':
        if queryset.count() > 1000:
            return JsonResponse({"message": "Cannot download more than 1000 rows at a time, please lower the search query."}, status=400)

        serializer = SerializerClass(queryset, many=True, context={'request': request, 'dataType': 'values'})
        return JsonResponse({"data": serializer.data})

    if requestType == "get_ids_list":
        if queryset.count() > 10000:
            return JsonResponse({"message": "10000 items allowed at max, please lower the search query."}, status=400)

        return JsonResponse({"data": list(queryset.values_list('id', flat=True))})

    # Pagination
    draw = int(request.GET.get("draw", 0))
    start = int(request.GET.get("start", 0))
    length = int(request.GET.get("length", 10))
    if length > 1000:
        length = 1000

    data = queryset.distinct()[start: start + length]
    total_records = queryset.count()

    serializer = SerializerClass(data, many=True, context={'request': request, 'dataType': 'input'})
    serialized_data = serializer.data
    return JsonResponse(
        {"draw": draw, "recordsTotal": total_records, "recordsFiltered": total_records, "data": serialized_data}
    )
