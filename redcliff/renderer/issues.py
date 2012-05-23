from clint.textui import puts


def as_table(data):
    offset = data['offset']
    limit = data['limit']
    total = data['total_count']
    first = offset + 1
    last = offset + limit if offset + limit <= total else total
    issues = data['issues']

    if not total:
        puts('No issues matching your query.')
    else:
        puts('Showing {first} - {last} of {total} total.'
             .format(first=first, last=last, total=total))

        for i in issues:
            puts('{id} | {status} | {priority} | {project} | {subject}'
                 .format(id=i['id'],
                         status=i['status']['name'],
                         priority=i['priority']['name'],
                         project=i['project']['name'],
                         subject=i['subject']))
