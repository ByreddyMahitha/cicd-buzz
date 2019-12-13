import requests
import json
from requests.auth import HTTPBasicAuth
import config


def construct_url(repo, path, name):
    file_stats_path = 'storage/{}?stats'.format(repo + '/' + path + '/' + name)
    return config.api_url.format(file_stats_path)


def get_maven_artifacts():
    data = 'items.find({"repo":{"$eq":"jcenter-cache"}})'
    try:
        r = requests.post(url=config.api_url.format('search/aql/'), data=data, auth=HTTPBasicAuth(config.username, config.password))
    except Exception as e:
        print "Exception {}".format(e)
    results = json.loads(r.content)['results']
    return results


def get_file_stats_for_artifacts():
    artifacts = get_maven_artifacts()
    download_list = []
    for item in artifacts:
        new_url = construct_url(item['repo'], item['path'], item['name'])
        try:
            resp = requests.get(url=new_url, auth=HTTPBasicAuth(config.username, config.password), timeout=5)
            content = json.loads(resp.content)
        except Exception as e:
            print "Exception {}".format(e)
            continue
        if content['downloadCount'] > 0:
            download_list.append(content)
    return download_list


def get_most_popular_artifacts(artifacts_list):
    sorted_list = sorted(artifacts_list, key=lambda i: (i.get('downloadCount'), i.get('lastDownloaded')), reverse=True)
    return sorted_list[0], sorted_list[1]


def main():
    filtered_list = get_file_stats_for_artifacts()
    first, second = get_most_popular_artifacts(filtered_list)
    print first
    print second

if __name__ == "__main__":
    main()
