from pyramid.security import Allow


SHARING_ATTR = "_sharing"


def add_sharing(event):

    """ Add any shares to ACL """

    shares = getattr(event.context, SHARING_ATTR, {})

    for user_id in shares.get('admin', []):
        event.acl.append((Allow, user_id, ('view', 'edit')))
        
    for user_id in shares.get('editors', []):
        event.acl.append((Allow, user_id, ('view', 'edit')))
            
    for user_id in shares.get('viewers', []):
        event.acl.append((Allow, user_id, 'view'))
