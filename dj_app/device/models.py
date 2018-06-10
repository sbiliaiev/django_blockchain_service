from django.db import models


class Device(models.Model):
    deviceId = models.CharField(max_length=32)


class DeviceData(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    rvc_as = models.TextField()
    ctx_era = models.TextField()
    cnt = models.FloatField()
    mix_stp = models.IntegerField()
    mux_delta_vp = models.FloatField()
    coef_ttx = models.FloatField()
    active = models.BooleanField()
