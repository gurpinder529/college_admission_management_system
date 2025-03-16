from  django.urls  import path, include
from . import views
urlpatterns = [
    path("",views.landingpage),
    path("about",views.aboutPage),
    path("category",views.categoryPage),
    path("contact",views.contactpage),
    path("job-detail",views.jobdetailpage),
    path("job-list",views.joblistpage),
    path("testimonial",views.testimonial),
    path("resume_upload",views.resume_upload),
    path("registration_form",views.registrationform),
    path("dashboard",views.dashboardpage),
]