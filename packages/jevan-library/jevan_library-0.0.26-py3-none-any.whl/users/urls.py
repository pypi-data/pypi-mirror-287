# from rest_framework import routers
from .views import InvitationViewSet, accept_invitation, UserViewSet, GroupViewSet, PermissionViewSet, ContenttypeViewSet, GroupOptionsViewSet, CUserViewSet, CGroupViewSet, signup,UserTokenPairView,APILogoutView
from django.urls import include, re_path as url
from xtrm_drest.routers import DynamicRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
# router = routers.SimpleRouter()
router = DynamicRouter()
router.register('users', UserViewSet)
router.register('edit/user', CUserViewSet)
router.register('groups', GroupViewSet)
router.register('edit/group', CGroupViewSet)
router.register('permissions', PermissionViewSet)
router.register('contenttypes', ContenttypeViewSet)
router.register('groupoptions', GroupOptionsViewSet)
router.register('invitations', InvitationViewSet)
invitations_patterns = (
    [
        url(
            r'^{0}/{1}/(?P<key>\w+)/?$'.format(
                'invitations', 'verify'
            ),
            accept_invitation,
            name='accept-invite'
        ),
        url(
            r'^{0}/{1}/(?P<key>\w+)/?$'.format(
                'invitations', 'signup'
            ),
            signup,
            name='signup-invite'
        ),
    ],
    'invitations'
)

urlpatterns = router.urls + [
    url(r'^', include(invitations_patterns)),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', UserTokenPairView.as_view(), name='token_obtain_pair'),
    path('logout/', APILogoutView.as_view(), name='logout_token'),
]
