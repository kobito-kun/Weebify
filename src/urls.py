"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from weeb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ViewMainPage, name="main"),
    
    path('@<str:user>', viewUserMain),
    path('@<str:user>/<str:type>', ViewType),

    path('register/', signUpPage, name="signup"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),

    path('dashboard/', dashboardPage, name="dashboard"),
    path('dashboard/posts', postsDashboardPage, name="dashboardedit"),
    path('dashboard/posts/add', addPostDashboardPage, name="dashboardadd"),
    path('dashboard/posts/delete/<int:id>', deleteDashboardPostPage, name="deletePost"),

    #scraped
    path('section/<str:type>', ViewType),
    path('post/<int:postID>', ViewPost),
    path('all/', ViewAll),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
