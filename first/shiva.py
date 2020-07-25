from django.http import HttpResponse
from django.shortcuts import render
import operator
def ram(request):
      return render(request,"c.html")

def aboutus(request):
      return render(request,"aboutus.html")




#def wel(request):
 #   return HttpResponse("<h1>shivadass</h1>")
#def hi(request):
 #   return render(request,"blink.html",)

  

def count(request):
      mess=request.GET['message']
      wl=mess.split()
      #print(wl)
      wlcount={}
      for word in wl:
            if word in wlcount:
                  wlcount[word] += 1
            else:
                  wlcount[word]=1
      sort1=sorted(wlcount.items(),key=operator.itemgetter(1),reverse=True)
      return render(request,"cr.html",{"msg":mess,"length":len(wl),"abc":wlcount,'cba':sort1})

