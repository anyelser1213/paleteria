from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.



##################################################################################################
####################### Modelos para Usuarios ####################################################

class UsuarioManager(BaseUserManager):

    def create_user(self,email,username,rol,password = None,admin = False,is_superuser =False):
        print("Creamos Usuario Normal")
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')

        usuario = self.model(
            
            username = username,
            email = self.normalize_email(email),
            rol = rol,
            admin =admin,
            is_superuser = is_superuser
        )

        #aqui encriptamos la clave para no guardar en texto plano
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    

    #Funcion para usuario administrador
    def create_superuser(self,email,username,rol,password,admin = True,is_superuser = True):
        print("Creamos superusuario")
        usuario = self.create_user(
            email = email,  
            username = username,
            rol = rol,
            password = password,
            admin =admin,
            is_superuser = is_superuser
        )
        
            
            
        print("Entramos en superuser")
        input()
        usuario.save()
        return usuario



# Heredamos de AbstractBaseUser para adaptarlo a nuestro gusto
class Usuarios(AbstractBaseUser,PermissionsMixin):

    usuario_tipos = [
        ('master','Master'),
        ('usuario','Usuario')
    ]
    
    
    username = models.CharField("Username",max_length=200,unique=True)
    nombres = models.CharField("Nombres",max_length=200,blank=True, null=True) 
    apellidos = models.CharField("Apellidos",max_length=200,blank=True, null=True) 
    email = models.EmailField("Correo Electronico",max_length=150, unique=True)
    #compañia = models.ForeignKey(Compañia,on_delete=models.CASCADE,blank=True, null=True)
    activo = models.BooleanField(default=True)   
    is_superuser = models.BooleanField(default=False)#Este es superusuario
    admin = models.BooleanField(default=False)#Para poder ingresar al admin de django
    cedula = models.IntegerField(default=0,blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    fecha_actualizacion = models.DateTimeField('actualizado', auto_now=True)
    direccion = models.CharField("Direccion",max_length=100,blank=True, null=True,default="Las Adjuntas") 
     
    
    rol = models.CharField("Rol",
        max_length=150,
        choices=usuario_tipos,    
        default='usuario'
    )
    telefono = models.CharField("Telefono", max_length=50,blank=True,null=True,default="04242020470")
    imagen = models.ImageField("Imagen de perfil", upload_to="usuario/perfil/", max_length=200,blank=True,null=True)
    
    #Para enlazar al manager que has creado
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'  #Para estableccer este campo como unico
    REQUIRED_FIELDS = ['email','rol','is_superuser','admin'] # Campos obligatorios(los pide cuando los creas por consola)

    def __str__(self):
        return f'Usuario {self.username}'
    
    
    
    #para verificar si un usuario es administrador o no(Para entrar en el admin)
    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         return self.admin
     

    def has_module_perms(self, app_label):
        return True



    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'
        
        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            #Permisos para master y gerente
            #("permisoscompletos", "Permisoscompletos"),
            
            
            
            
            
            
        ]#Fin de los permisos


##########################################################################################################
##########################################################################################################
