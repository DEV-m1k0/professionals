from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    OrganizationListApiView, SubDivisionListApiView, SubSubDivisionListApiView,
    EmployeeListApiView, EmployeeSearchApiView
    )

urlpatterns = [
    path('SignIn', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("Document", include("document.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path("organizations", OrganizationListApiView.as_view()),
    path("subdivisions", SubDivisionListApiView.as_view()),
    path("subsubdivions", SubSubDivisionListApiView.as_view()),
    path("employees", EmployeeListApiView.as_view()),
    path("employees/search/<str:department>", EmployeeSearchApiView.as_view()),
]