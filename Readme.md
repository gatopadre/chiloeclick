# proyecto chiloe click

## requisitos previos
    - python
    - flask

## comando gcloud
gcloud compute instances create server-ubuntu --project=servidor-principal-352701 --zone=us-central1-a --machine-type=e2-micro --network-interface=network-tier=PREMIUM,subnet=default --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=236868335652-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --create-disk=auto-delete=yes,boot=yes,device-name=server-ubuntu,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20220606,mode=rw,size=10,type=projects/servidor-principal-352701/zones/us-central1-a/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any

## costos
google cloud: 8 usd mes
maphub:

## TODOs:
- Logo completo Chiloeclik
- BD para almacenar mensajes.
- Correo receptor de los mensajes.
- Logica para el envio de los mensajes del formulario de contacto.