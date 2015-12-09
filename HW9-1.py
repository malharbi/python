import psutil
import datetime
from wsgiref.simple_server import make_server

def system_Information(environ, start_response):
	htmlCode=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	network = psutil.net_io_counters()
	disk = psutil.disk_io_counters()
	diskSize = psutil.disk_usage('/')

	start_response(status, headers)
	htmlCode += "<h1>System Information</h1>"
	htmlCode += """<div>
					<div id="586417348255479931" align="left" style="width: 100%;overflow-y: hidden;" class="wcustomhtml">
						<table width='40%' border=0>
							<tr bgcolor='#C0C0C0'>
								<td>BOOT TIME</td>
								<td>"""+str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))+"""</td>
							</tr>
							<tr>
								<td>Network Information</td>
								<td>
									<table border=0 width='100%'>
										<tr>
											<td>Mbytes sent</td>
											<td bgcolor='#FF4500'>"""+str(network.bytes_sent//1000000)+"""</td>
										</tr>
										<tr>
											<td>Mbytes received </td>
											<td bgcolor='#FF4500'>"""+str(network.bytes_recv//1000000)+"""</td>
										</tr>
										<tr>
											<td>Packets sent</td>
											<td bgcolor='#FF4500'> """+str(network.packets_sent)+"""</td>
										</tr>
										<tr>
											<td>Packets received</td>
											<td bgcolor='#FF4500'> """+str(network.packets_recv)+"""</td>
										</tr>
										<tr>
											<td>Errors while receiving</td>
											<td bgcolor='#FF4500'> """+str(network.errin)+"""</td>
										</tr>
										<tr>
											<td>Errors while sending</td>
											<td bgcolor='#FF4500'> """+str(network.errout)+"""</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td>Disk Information</td>
								<td>
									<table border=0 width='100%'>
										<tr>
											<td>Total</td>
											<td bgcolor='FFFF00'>"""+str(diskSize.total//1000000000)+""" GB</td>
										</tr>
										<tr>
											<td>Used  </td>
											<td bgcolor='FFFF00'>"""+str(diskSize.used//1000000000)+""" GB</td>
										</tr>
										<tr>
											<td>Free</td>
											<td bgcolor='FFFF00'> """+str(diskSize.free//1000000000)+""" GB</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td>Reading from disk</td>
								<td>"""+str(disk.read_time//167000)+""" minutes</td>
							</tr>
							<tr bgcolor='#C0C0C0'>
								<td>Writing to disk</td>
								<td>"""+str(disk.write_time//167000)+""" minutes</td>
							</tr>
						</table>
					</div>
				</div>
				"""
	return[bytes(htmlCode,'utf-8')]
		
httpd = make_server('', 8000, system_Information)
print("Serving on http://127.0.0.1:8000/...")

httpd.serve_forever()
