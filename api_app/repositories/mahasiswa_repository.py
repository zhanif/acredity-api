import bcrypt
from ..models.mahasiswa import Mahasiswa
from ..serializers.mahasiswa_serializer import MahasiswaSerializer

class MahasiswaRepository:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

  def find_all(self):
    mahasiswa = Mahasiswa.objects.all()
    serializer = MahasiswaSerializer(mahasiswa, many=True)
    return serializer.data
  
  def find_by_nim(self, nim):
    try:
      mahasiswa = Mahasiswa.objects.get(nim=nim)
      serializer = MahasiswaSerializer(mahasiswa)
      return serializer.data
    except Mahasiswa.DoesNotExist:
      return None

  def create(self, data):
    password = data.pop('password')
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    data['password'] = hashed_password.decode()

    serializer = MahasiswaSerializer(data=data)
    if serializer.is_valid():
      mahasiswa = serializer.save()
      return mahasiswa.id
    return None

  def update(self, nim, data):
    try:
      mahasiswa = Mahasiswa.objects.get(nim=nim)
      password = data.pop('password', None)
      if password is not None:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        data['password'] = hashed_password.decode()

      serializer = MahasiswaSerializer(instance=mahasiswa, data=data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return True
      return False
    except Mahasiswa.DoesNotExist:
      return False

  def delete(self, nim):
    try:
      mahasiswa = Mahasiswa.objects.get(nim=nim)
      mahasiswa.delete()
      return True
    except Mahasiswa.DoesNotExist:
      return False
