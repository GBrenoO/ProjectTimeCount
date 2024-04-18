from datetime import datetime
from dateutil.relativedelta import relativedelta

paused = False
have_return = False

while True:
    
    MENU = input('MENU: \n '
                 '\t INICIAR|I \n '
                 '\t PAUSAR|P \n'
                 '\t VOLTAR|V \n'
                 '\t FINALIZAR|F \n'
                 '\t VER TEMPO|T \n ').upper()
    
    
    if MENU == 'I':
        
        def iniciar():
            iniciar = datetime.now()
            return iniciar
        
        moment_init = iniciar()
        print(moment_init)
        
        
    if MENU == 'P':
        
        def pausar():
            paused = True
            pausar = datetime.now()
            return pausar
        
        paused = True   
        have_return = False  
        pause = pausar()
        print(pause)
        
        
    if MENU == 'V':
        
            if paused:
                def voltar():
                    have_return = True
                    paused = False
                    return datetime.now()
                
                voltar = voltar() 
                have_return = True
                paused = False
                time_pausing = voltar - pause
                print(voltar)


    if MENU == 'F':
        def finalizar():
            return datetime.now()
        moment_final = finalizar()
        print(moment_final)

        def result ():
            time_studing = moment_final - moment_init
            view_time = datetime.now() - moment_init
            
            if paused:
                time_is_pause = datetime.now() - pause
                result_is_pause = view_time - time_is_pause 
                return result_is_pause
            
            if have_return:
                time_pausing = voltar - pause
                result_is_pause = time_studing - time_pausing
                return result_is_pause
            
            return time_studing
        
        resulted = result()
        print(resulted)
        break
    
    
    if MENU == 'T':
        
        def view_time():
            view_time = datetime.now() - moment_init
            
            if paused:
                time_is_pause = datetime.now() - pause
                view_time_is_pause = view_time - time_is_pause 
                return view_time_is_pause
            
            if have_return:
                time_is_init = datetime.now() - moment_init 
                view_time_is_return = time_is_init - time_pausing  
                return view_time_is_return
            
            return view_time
        
        view_time = view_time()
        print(view_time)