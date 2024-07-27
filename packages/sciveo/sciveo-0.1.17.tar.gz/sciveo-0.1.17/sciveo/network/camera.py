import threading
import cv2
import numpy as np

from sciveo.common.tools.logger import *
from sciveo.common.tools.timers import FPSCounter
from sciveo.network.tools import StreamSniffer


class RTSPStreamSniffer(StreamSniffer):
  def on_packet(self, packet):
    if self.is_rtsp_packet(packet):
      self.append_ip_packet(packet)

  def is_rtsp_packet(self, packet):
    return IP in packet and TCP in packet and (packet[TCP].dport == 554 or packet[TCP].sport == 554)

  def get_rtsp_frames(self, ip_src):
    frames = []
    current_packets = self.get_ip_stream(ip_src)
    for packet in current_packets:
      frame = self.packet_to_frame(packet)
      if frame is not None:
        frames.append(frame)
    return frames

  def packet_to_frame(self, packet):
    payload = bytes(packet[TCP].payload)
    nparr = np.frombuffer(payload, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return frame

  def play(self, ip_src):
    fps = FPSCounter(tag=f"play {ip_src}")
    while True:
      frames = self.get_rtsp_frames(ip_src)
      for frame in frames:
        fps.update()
        cv2.imshow(f'RTSP Stream from {ip_src}', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
          return


if __name__ == '__main__':
  sniffer = RTSPStreamSniffer(iface="eth0")
  sniffer.start()

  camera_ips = []

  threads = []
  for ip in camera_ips:
    t = threading.Thread(target=sniffer.play, args=(ip,))
    t.start()
    threads.append(t)

  try:
    while True:
      pass
  except KeyboardInterrupt:
    sniffer.stop_sniffing()
    for t in threads:
      t.join()
    cv2.destroyAllWindows()
