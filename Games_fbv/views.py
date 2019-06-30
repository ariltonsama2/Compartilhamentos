from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django import forms
from Games_fbv.models import Game

#Form de cadastro de jogo
class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'contato','originalum','originaldois','fantasma','senha']  
        labels = {
            "originalum": "Original Um",
            "originaldois": "Original Dois",
            "fantasma": "Fantasma",
        }
    # Validação
    def is_valid(self):
        
        valid = super(GameForm, self).is_valid()
        
        if not valid:
            return valid
        #Valida se contato é um numero valido (não possui letras)
        contato = self.cleaned_data['contato']
        try: 
            int(contato)
            if(self.cleaned_data['originalum'] == 0 and self.cleaned_data['originaldois'] == 0 and self.cleaned_data['fantasma'] == 0):
                self.add_error('originalum','Ao menos um dos valores deve ser diferente de zero')
                return False
            return True
        except ValueError:
            self.add_error('contato', 'Digite apenas números')
            return False
            
        
    
 #Form de edição de jogo
class GameFormEdit(ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'contato','originalum','originaldois','fantasma','senha']
        labels = {
            "originalum": "Original Um",
            "originaldois": "Original Dois",
            "fantasma": "Fantasma",
        }
    #Validação
    def is_valid(self,aux):
        
        valid = super(GameFormEdit, self).is_valid()
        
        if not valid:
            return valid
        #Validação da senha
        if (self.cleaned_data['senha'] != aux):
            self.add_error('senha', 'Senha incorreta')
            return False
            
        contato = self.cleaned_data['contato']
        try: 
            int(contato)
            if(self.cleaned_data['originalum'] == 0 and self.cleaned_data['originaldois'] == 0 and self.cleaned_data['fantasma'] == 0):
                self.add_error('originalum','Ao menos um dos valores deve ser diferente de zero')
                return False
            return True
        except ValueError:
            self.add_error('contato', 'Digite apenas números')
            return False
        
        return True
  
#Form de deletar jogo 
class GameFormDelete(ModelForm):
    class Meta:
        model = Game
        fields = ['senha']
        
    def is_valid(self,aux):
        
        valid = super(GameFormDelete, self).is_valid()
        
        if not valid:
            return valid
        #Validação da senha
        if (self.cleaned_data['senha'] != aux):
            self.add_error('senha', 'Senha incorreta')
            return False    
        return True

def Game_list(request, template_name='Games_fbv/Game_list.html'):
    game = Game.objects.all()
    data = {}
    data['object_list'] = game
    return render(request, template_name, data)

def Game_create(request, template_name='Games_fbv/Game_form.html'):
    game = Game()
    game.contato = "Digite telefone com ID do país e DDD"
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('Games_fbv:Game_list')
    
    return render(request, template_name, {'form':form})

def Game_update(request, pk, template_name='Games_fbv/Game_form.html'):
    game = get_object_or_404(Game, pk=pk)
    aux = game.senha
    game.senha = "Digite a senha correta"
    form = GameFormEdit(request.POST or None, instance=game)
    if form.is_valid(aux):
        form.save()
        return redirect('Games_fbv:Game_list')
    else:
        
        return render(request, template_name, {'form':form})

def Game_delete(request, pk, template_name='Games_fbv/Game_confirm_delete.html'):
    game = get_object_or_404(Game, pk=pk) 
    aux = game.senha
    game.senha = "Digite a senha correta"
    form = GameFormDelete(request.POST or None, instance=game)    
    if form.is_valid(aux):
        game.delete()
        return redirect('Games_fbv:Game_list')
    return render(request, template_name, {'form':form})
