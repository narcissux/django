import hmac
from git import Repo
from django.http import HttpResponse


# github的webhook请求处理
def handle_github_hook(request):
    signature = request.META['HTTP_X_HUB_SIGNATURE']
    if signature.find('=')>=0:
        sha, signature = signature.split('=')
    secret = str.encode("galgameplay")
    hashhex = hmac.new(secret, request.body, digestmod='sha1').hexdigest()
    if hmac.compare_digest(hashhex, signature):
        repo = Repo('/home/gwt/sites/docker.narcissu.tk/django/')
        origin = repo.remotes.origin
        origin.pull('--rebase')
        commit = request.json['after'][0:6]
        print('Repository updated with commit {}'.format(commit))
        return HttpResponse('', status=200)
    return HttpResponse('', status=400)
