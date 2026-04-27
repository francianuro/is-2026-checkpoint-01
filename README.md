# is-2026-checkpoint-01
Trabajo practico grupal para la materia ingenieria de software - UTN FRLP - 2026


## Panel de Monitoreo: Portainer
- **Acceso**: `http://localhost:9000`
- **Usuario**: El que crees en el primer inicio
- **Función**: Interfaz web para ver, reiniciar y monitorear los contenedores del proyecto sin usar terminal.
- **Persistencia**: Configuración guardada en el volumen nombrado `portainer_data`.
- **Socket**: Monta `/var/run/docker.sock` para comunicarse directamente con el daemon de Docker.