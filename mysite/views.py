from django.http import HttpResponse
from django.shortcuts import render

              








def index(request):
    print(request.POST.get('text','defaault'))
    return render(request,'index.html')
    
    return HttpResponse("home")
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
  
    analyzed=djtext
    if removepunc=="on":
         punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
         analyzed=""
         for char in djtext:
             if char not in punctuation:
                 analyzed=analyzed+char
         params={'purpose':'removed punctuatoions', 'analyzed_text':analyzed}
         djtext=analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
            params={'purpose':'change to uppercase', 'analyzed_text':analyzed}
            djtext=analyzed
    if(newlineremover=="on"):
          analyzed=""
          for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
            params={'purpose':'remove new line', 'analyzed_text':analyzed}
            djtext=analyzed
    if(extraspaceremover=="on"):
           analyzed=""
           for index,char in enumerate(djtext):
            if djtext[index]== " " and djtext[index+1]==" ":
                pass
            else: analyzed = analyzed + char
            params={'purpose':'remove new line', 'analyzed_text':analyzed}
           djtext=analyzed
    if(removepunc!="on"and newlineremover!="on"and extraspaceremover!="on"and fullcaps!="on"):
        return HttpResponse("error")       
     
    return render(request,'analyze.html',params)
   
   
          
   
    
      
            
