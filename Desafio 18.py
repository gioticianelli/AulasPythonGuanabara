import math

ang = float(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(ang))  # math.radians vai converter em radianos
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}\n'
      'O ângulo de {} tem COSSENO de {:.2f}\n'
      'O ângulo de {} tem TANGENTE de {:.2f}'.format(ang, sen, ang, cos, ang, tan))