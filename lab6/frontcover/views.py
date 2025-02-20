# frontcover/views.py
from django.shortcuts import render
from .forms import MagazineForm
from PIL import Image, ImageDraw, ImageFont
import io
from django.http import HttpResponse

def magazine_cover(request):
    if request.method == "POST":
        form = MagazineForm(request.POST, request.FILES)
        
        if form.is_valid():
            title = form.cleaned_data['title']
            subtitle = form.cleaned_data['subtitle']
            image = form.cleaned_data['image']
            bg_color = form.cleaned_data['bg_color'] or '#FFFFFF'  # Default white if not provided
            font_size = form.cleaned_data['font_size']
            font_color = form.cleaned_data['font_color'] or '#000000'  # Default black if not provided

            # Load the uploaded image
            img = Image.open(image)
            img = img.resize((800, 1200))  # Resize the image to fit the cover proportionally

            # Create a drawing object
            draw = ImageDraw.Draw(img)

            # Load font (use a built-in font for simplicity)
            font_path = '/home/student/Desktop/wp_lab5/lab6/frontcover/static/frontcover/FreeMono.ttf'  # Replace with the actual font path
            font = ImageFont.truetype(font_path, font_size)

            # Add text to the image
            draw.text((50, 50), title, font=font, fill=font_color)
            draw.text((50, 150), subtitle, font=font, fill=font_color)

            # Convert the image to a file-like object
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)

            # Return the image as a response
            return HttpResponse(img_byte_arr, content_type='image/png')

    else:
        form = MagazineForm()

    return render(request, 'frontcover/index.html', {'form': form})
