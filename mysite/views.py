from django.http import HttpResponse
from django.shortcuts import render
# def ex1(request):
#      s=['''Navigation Bar <br> </h2>
#     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
#     <a href="https://www.facebook.com/"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/"> News </a> <br>
#     <a href="https://www.google.com/"> Google </a> <br>''']
#      return HttpResponse((s))
              


# def index(request):
#     return HttpResponse("<h1>hello anurag</h1>")
# def about(request):
#     return HttpResponse(" anurag")





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
    #charcount=request.POST.get('charcount','off')
  
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
   
   
          
   
    
      
            
