from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'first.html')

def analyze(request):
    
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extra_space_remover=request.POST.get('extra_space_remover','off')
    char_counter=request.POST.get('char_counter','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc=='on':
        print(removepunc)
      
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
             analyzed=analyzed+char
        
        params={'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        djtext=analyzed
    if(fullcaps=='on'):
       analyzed='' 
       for char in djtext:
          analyzed=analyzed+char.upper()

       params={'purpose':'Change To UpperCase', 'analyzed_text':analyzed}
       djtext=analyzed
      
    if(newlineremover=='on'):
       analyzed='' 
       for char in djtext:
          if char!='\n' and char!='\r':
            analyzed=analyzed+char

       params={'purpose':'New Line Removed', 'analyzed_text':analyzed}
       djtext=analyzed
            
    if(extra_space_remover=='on'):
       analyzed='' 
       for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
              pass
            else:
               analyzed=analyzed+char

       params={'purpose':'Extra Space Removed', 'analyzed_text':analyzed}
       
       djtext=analyzed
   #  if(char_counter=='on'):
   #     analyzed=len(djtext)
       
          

   #     params={'purpose':'Count Characters', 'analyzed_text':analyzed}
   #     djtext=analyzed
      
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extra_space_remover!='on' ):
       return HttpResponse("Error!")
    
    
    return render(request,'analyze.html',params)
        

