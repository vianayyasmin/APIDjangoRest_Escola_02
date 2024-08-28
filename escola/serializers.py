from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']
        
        def validate(self,dados):
            if nome_invalido (dados['nome']):
                raise serializers.ValidationError({'nome':'O nome só pode conter letras!'})
            
            if cpf_invalido(dados['cpf']) !=11:
                raise serializers.ValidationError({'cpf':'O CPF deve ser um valor válido!'})
            
            if celular_invalido(dados['celular']) !=13:
                raise serializers.ValidationError({'celular':'O celular deve seguir o modelo: 85 99999-9999. Respeitando traços e espaços!'})
            return dados
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []
        
class MatriculaEstudanteSerializer(serializers.ModelSerializer):
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['id', 'estudante', 'curso', 'periodo']

    def get_periodo(self, obj):
        return obj.periodo
    
class MatriculaCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
        
class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
                model = Estudante
    fields = ['id', 'nome', 'email','celular']
