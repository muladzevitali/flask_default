import json


def create_users(user_model, role_model, db):
    """Inserting Administrators and users when starting the server"""
    with open("media/database/users_tree.json") as input_stream:
        users_tree = json.load(input_stream)
    admin_role = role_model(name='admin', description='Super user privileges')
    db.session.add(admin_role)

    for user_meta in users_tree:
        user = user_model()
        user.first_name = user_meta["first_name"]
        user.last_name = user_meta["last_name"]
        user.id = user_meta["id"]
        user.manager_id = user_meta["manager_id"]
        user.email = user_meta["email"]
        user.username = user_meta["email"].split("@")[0]
        user.password = user.hash_password(user_meta['password'])

        if user_meta.get('is_admin', False):
            user.roles.append(admin_role)
        db.session.add(user)

    db.session.commit()
