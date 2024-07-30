from maeser.user_manager import UserManager
from flask import abort, request

def controller(user_manager: UserManager):
    """
    API endpoint for user management.

    Args:
        user_manager (UserManager): User Manager object to interact with the user database.

    """
    if not request.is_json or request.json is None:
        return abort(400, 'Request must be JSON')
    command = request.json.get('type')
    auth_method = request.json.get('user_auth', '')
    user_ident = request.json.get('user_id', '')
    print(f'{type(command)}: {command}')
    print(request.json)
    if command == 'list-users':
        # get arguments for the filter by auth, admin, and banned status
        auth_filter = request.json.get('auth-filter', 'all')
        admin_filter = request.json.get('admin-filter', 'all')
        banned_filter = request.json.get('banned-filter', 'all')
        user_list = [user.json for user in user_manager.list_users(auth_filter, admin_filter, banned_filter)]
        return user_list
    elif command == 'toggle-admin':
        new_status = request.json.get('new_status')
        if new_status is None:
            return abort(400, 'Missing new_status')
        user_manager.update_admin_status(auth_method, user_ident, new_status)
        return {'response': f'Made {auth_method}.{user_ident} {"an admin" if new_status else "no longer an admin"}'}
    elif command == 'toggle-ban':
        new_status = request.json.get('new_status')
        if new_status is None:
            return abort(400, 'Missing new_status')
        user_manager.update_banned_status(auth_method, user_ident, new_status)
        return {'response': f'Made {auth_method}.{user_ident} {"an banned" if new_status else "no longer an banned"}'}
    elif command == 'update-requests':
        sub_action = request.json.get('action')
        if sub_action is None:
            return abort(400, 'Missing action')
        if sub_action == 'add':
            user_manager.increase_requests(auth_method, user_ident)
        elif sub_action == 'remove':
            user_manager.decrease_requests(auth_method, user_ident)
        else:
            return abort(400, f'Invalid action was given: "{sub_action}"')
        return {'response': f'Updated {auth_method}.{user_ident} requests'}
    elif command == 'remove-user':
        user_manager.remove_user_from_cache(auth_method, user_ident)
        return {'response': f'Removed {auth_method}.{user_ident} from the cache'}
    elif command == 'fetch-user':
        user_manager.fetch_user(auth_method, user_ident)
        return {'response': f'Fetched {auth_method}.{user_ident}'}
    elif command == 'list-cleanables':
        return user_manager.list_cleanables()
    elif command == 'clean-cache':
        user_manager.clean_cache()
        return {'response': 'Cleaned user cache'}
    else:
        return abort(400, f'Invalid command type was given: "{command}"')