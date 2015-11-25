def set_hadoop_config(credentials):
    prefix = "fs.swift.service." + credentials['name'] 
    hconf = sc._jsc.hadoopConfiguration()
    hconf.set(prefix + ".auth.url", credentials['auth_url']+'/v2.0/tokens')
    hconf.set(prefix + ".auth.endpoint.prefix", "endpoints")
    hconf.set(prefix + ".tenant", credentials['project_id'])
    hconf.set(prefix + ".username", credentials['user_id'])
    hconf.set(prefix + ".password", credentials['password'])
    hconf.setInt(prefix + ".http.port", 8080)
    hconf.set(prefix + ".region", credentials['region'])
    hconf.setBoolean(prefix + ".public", True)

credentials = {}
credentials['name'] = 'keyfactor'
credentials['auth_url'] = 'https://identity.open.softlayer.com'
credentials['project_id'] = 'e6a01c4a648a4e20a1db088ee16b54c8'
credentials['region'] = 'dallas'
credentials['user_id'] = 'eeb49d62fd6a4fbd8930762fe3e81297'
credentials['password'] = 'Rad..UiEk^o}=8.0'

set_hadoop_config(credentials)



