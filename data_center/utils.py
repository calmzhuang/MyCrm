from data_center.models import DatabaseConfig

def data_config_list():
    data_list = DatabaseConfig.objects.values()
    return data_list

def create_data_config_list(data):
    filter_conditions = {}
    result = DatabaseConfig.objects.filter(name=data.get('name'))
    if not result.exists():
        for k, v in data.items():
            filter_conditions[k] = v
        DatabaseConfig.objects.create(**filter_conditions)
        return 'success'
    else:
        return 'fail'

def update_data_config_list(data):
    filter_conditions = {}
    result = DatabaseConfig.objects.filter(name=data.get('name'))
    if result.exists():
        for k, v in data.items():
            filter_conditions[k] = v
        result.update(**filter_conditions)
        return 'success'
    else:
        return 'fail'
