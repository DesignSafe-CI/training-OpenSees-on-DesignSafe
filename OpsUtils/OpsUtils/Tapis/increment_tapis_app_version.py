def increment_tapis_app_version(t,app_id):
    from OpsUtils import OpsUtils
    results = t.apps.getApps()
    foundIt = False
    for thisRes in results:
        here_id = thisRes.id
        if here_id == app_id:
            foundIt = True
    if foundIt:
        latest_app_version = OpsUtils.get_latest_app_version(t,app_id)
        print('app exists, now latest_app_version',latest_app_version)
        app_version = OpsUtils.bump_app_version(latest_app_version,'patch')
    else:
        print('new app')
        app_version = '0.0.1'
    print('now app_version',app_version)
    return app_version