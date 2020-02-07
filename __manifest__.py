{
    "name": "FeesCollection",
    "version": "1.0",
    "depends": ["web", "base", "web_dashboard","portal"],
    "data": [
        "security/security_fees_collection.xml",
        "views/portal_user.xml",
        "security/ir.model.access.csv",
        "views/Institute_views.xml",
        "views/course.xml",
        "views/report.xml",
        "views/add_student.xml",
    ],
    "demo":
        [
        "demo/institute_demo.xml",
    ],

}
