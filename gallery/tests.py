from django.test import TestCase
from .models import Aquascape
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


# Testing for Aquascape model
class AquascapeModelTest(TestCase):
    def test_create_aquascape(self):
        image = SimpleUploadedFile("test.jpg", b'file_content', content_type="image/jpeg")
        aquascape = Aquascape.objects.create(
            title = "Test Tank",
            description = "A beautiful aquascape.",
            image = image
        )
        self.assertEqual(aquascape.title, "Test Tank")
        self.assertTrue(aquascape.created_at)
        
# Testing for Aquascape views
class GalleryTestView(TestCase):
    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
    def test_gallery_template_used(self):
        resonse = self.client.get(reverse('gallery'))
        self.assertTemplateUsed(resonse, 'gallery/gallery.html')
        