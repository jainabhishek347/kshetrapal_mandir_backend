from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

"""
Note: Real time example of middle ware:
1: Block IPS for all/specific request. 
2: Also we can block requests based on time interval eg: Max request per IP 10 every minute.
3: Log specific request params an use them for analysis perpose.
4: Excepetion handling for unhandelled requests.
5: Modify or Alter response of any request. 

"""

class FilterIPMiddleware(MiddlewareMixin):
	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	# def __call__(self, request):
	#   # Code to be executed for each request before
	#   # the view (and later middleware) are called.
	# 	If used with MIDDLEWARE_CLASSES, the __call__() method will never be used; 
	#	Django calls process_request() and process_response() directly.

	# 	response = self.get_response(request)
	# 	print('in middle ware calll')
	#     # Code to be executed for each request/response after
	#     # the view is called.

	# 	return response

	def process_request(self, request):
		allowed_ips = ['192.168.1.1', '123.123.123.123', '172.20.0.1', '0.0.0.0', '127.0.0.1'] # Authorized ip's
		ip = request.META.get('REMOTE_ADDR') # Get client IP
		#print('process_request: '  , ip)
		if ip not in allowed_ips:
			return HttpResponseForbidden() # If user is not allowed raise Error
		# If IP is allowed we don't do anything
		return None
	
	def process_view(self, request, view_func, view_args, view_kwargs):
		"""
		1: request is an HttpRequest object. view_func is the Python function that Django 
		is about to use. (It’s the actual function object, not the name of the function 
		as a string.) 
		
		2: view_args is a list of positional arguments that will be passed to the view, 
		and view_kwargs is a dictionary of keyword arguments 

		3: process_view() is called just before Django calls the view.
		"""
		pass
		#print("process_view: ", request, view_func, view_args, view_kwargs)

	def process_exception(self, request, exception):
		"""
		request is an HttpRequest object. exception is an Exception object raised 
		by the view function.
		Django calls process_exception() when a view raises an exception. process_exception() 
		should return either None or an HttpResponse object. If it returns an HttpResponse object, 
		the template response and response middleware will be applied
		"""
		pass
		#print("Exception: ", exception)

	def process_template_response(self, request, response):
		"""
		 response is the TemplateResponse object (or equivalent) returned by a Django view 
		 or by a middleware.
		 it is called just after the view has finished executing, if the response instance 
		 has a render() method, indicating that it is a TemplateResponse or equivalent.
		 It must return a response object
		"""
		#p
		#
		#
		#
		#
		# rint("process_template_response: ",response)
		return response

	def get_response(self, request):		
		#print('get_response ==========')
		pass

	def process_response(self, request, response):
		#print("process_response ===", response)
		return response		