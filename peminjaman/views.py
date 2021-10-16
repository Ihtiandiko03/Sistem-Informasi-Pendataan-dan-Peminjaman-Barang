from django.shortcuts import render, redirect
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
# Create your views here.
from .models import Peminjaman
from .models import DetailPeminjaman
from .forms import PeminjamanForm
from .forms import DetailPeminjamanForm
from django.db import connection

def list(request):
	cursor=connection.cursor()
	cursor.execute("SELECT peminjaman_detailpeminjaman.Nama_Pegawai, peminjaman_detailpeminjaman.Tgl_Pinjam, peminjaman_detailpeminjaman.Tgl_Kembali, peminjaman_detailpeminjaman.Berita_Acara_Peminjaman, peminjaman_peminjaman.Nama_Barang, peminjaman_peminjaman.Jumlah, peminjaman_peminjaman.Kondisi, peminjaman_peminjaman.Ruang_id, peminjaman_peminjaman.Gedung_id FROM peminjaman_detailpeminjaman JOIN peminjaman_peminjaman WHERE peminjaman_detailpeminjaman.No_Peminjaman=peminjaman_peminjaman.No_Peminjaman_id")
	results=cursor.fetchall()

	context = {
		'title' : 'Peminjaman Barang',
		'Peminjaman' : results,
	}

	return render(request, 'peminjaman/list.html',context)

def detail(request):

	context = {
		'title' : 'Halaman dialihkan, Silahkan mengisi form peminjaman di halaman selanjutnya',
	}
	return render(request, 'peminjaman/detail.html', context)

def create(request):
	akun_form = DetailPeminjamanForm(request.POST or None)
	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('http://127.0.0.1:8000/admin/peminjaman/peminjaman/add/')

	context = {
		'title' : 'Form Peminjaman Barang',
		'akun_form' : akun_form,
	}

	return render(request, 'peminjaman/create.html', context)

def delete(request, delete_id):
	Peminjaman.objects.filter(id=delete_id).delete()
	DetailPeminjaman.objects.filter(id=delete_id).delete()
	return redirect('peminjaman:list')

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('peminjaman/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('peminjaman/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Laporan Peminjaman_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response


cursor=connection.cursor()
cursor.execute("SELECT peminjaman_detailpeminjaman.Nama_Pegawai, peminjaman_detailpeminjaman.Tgl_Pinjam, peminjaman_detailpeminjaman.Tgl_Kembali, peminjaman_detailpeminjaman.Berita_Acara_Peminjaman, peminjaman_peminjaman.Nama_Barang, peminjaman_peminjaman.Jumlah, peminjaman_peminjaman.Kondisi, peminjaman_peminjaman.Ruang_id, peminjaman_peminjaman.Gedung_id FROM peminjaman_detailpeminjaman JOIN peminjaman_peminjaman WHERE peminjaman_detailpeminjaman.No_Peminjaman=peminjaman_peminjaman.No_Peminjaman_id")
results=cursor.fetchall()

data = {
	'title' : 'Peminjaman Barang',
	'Peminjaman' : results,
}

