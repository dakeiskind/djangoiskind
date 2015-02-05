from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render_to_response


_person_name = 'dakeiskind'

# Create your views here.
def index(request):
    return HttpResponse("Home Page")


def hello(request):
    return HttpResponse("Hello %s" % _person_name)


def current_datetime(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render_to_response("time/current/current_time.html", locals())


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False

    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    return render_to_response("time/time_plus/time_plus.html", locals())


def order_notice(request):
    # # file = 'templates/order_notice.html'
    # # try:
    # #     fp = open(file, 'r')
    # # except IOError:
    # #     raise Http404()
    # #
    # # tmpl = Template(fp.read())
    # # fp.close()
    # tmpl = loader.get_template('order_notice.html')
    #
    # html = tmpl.render(Context({
    #     'person_name': 'dakeiskind',
    #     'ship_date': datetime.datetime.now(),
    #     'item_list': ['iPhone 6', 'Nexus 6'],
    #     'company': 'HP',
    #     'ordered_warranty': True}))
    #
    # return HttpResponse(html)

    person_name = 'dAKE'
    ship_date = datetime.datetime.now()
    item_list = ['iPhone 6', 'Nexus 6']
    company = 'HP'
    ordered_warranty = True

    return render_to_response('order_notice.html', locals())


def delete(self):
    pass


delete.alters_data = True