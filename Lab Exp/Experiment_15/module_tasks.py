def create_task(title, assignee):
    if not title.strip(): raise ValueError('Task title is required')
    return {'title': title, 'assignee': assignee, 'status': 'To Do'}
