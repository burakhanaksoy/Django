from rest_framework import throttling


class StudentListUserThrottle(throttling.UserRateThrottle):
    scope = 'get_student_usr_throttle'

    def allow_request(self, request, view):
        return super().allow_request(request, view)


class StudentListAnonThrottle(throttling.AnonRateThrottle):
    scope = 'get_student_anon_throttle'

    def allow_request(self, request, view):
        return super().allow_request(request, view)
