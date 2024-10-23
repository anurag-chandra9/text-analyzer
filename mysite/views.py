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
    print(request.GET.get('text','defaault'))
    return render(request,'index2.html')
    
    return HttpResponse("home")
def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')
    print(removepunc)
    print(djtext) 
    analyzed=djtext
    if removepunc=="on":
         punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
         analyzed=""
         for char in djtext:
             if char not in punctuation:
                 analyzed=analyzed+char
         params={'purpose':'removed punctuatoions', 'analyzed_text':analyzed}
         return render(request,'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
            params={'purpose':'change to uppercase', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(newlineremover=="on"):
          analyzed=""
          for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
            params={'purpose':'remove new line', 'analyzed_text':analyzed}
          return render(request,'analyze.html',params)
    elif(extraspaceremover=="on"):
           analyzed=""
           for index,char in enumerate(djtext):
            if djtext[index]== " " and djtext[index+1]==" " :
                pass
            else: analyzed = analyzed + char
            params={'purpose':'remove new line', 'analyzed_text':analyzed}
           return render(request,'analyze.html',params)
    # elif(charcount=="on"):
    #     count=0
    #     for char in djtext:
    #         if char.isalpha():
    #             count+=1
    #         params={'purpose':'remove new line', 'analyzed_text':count}
    #     return render(request,'analyze.html',params)    

   
    else:
     return HttpResponse("ERROR")  
          
   
    
      
            
# def capfirst(request):
#     return HttpResponse("captalize first")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove")
# def charcount(request):
#     return HttpResponse("charcount")