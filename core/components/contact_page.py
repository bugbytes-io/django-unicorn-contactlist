from django_unicorn.components import UnicornView
from core.models import User


class ContactPageView(UnicornView):
    contact_pk = None
    contacts = User.objects.none()
    users = User.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.refresh_state()

    def add_contact(self):
        if self.contact_pk:
            self.request.user.contacts.add(self.contact_pk)
            self.refresh_state()

    def delete_contact(self, pk):
        self.request.user.contacts.remove(pk)
        self.refresh_state()


    def get_non_contacts(self):
        contact_pks = self.contacts.values_list('pk')
        return User.objects.exclude(pk=self.request.user.pk).exclude(pk__in=contact_pks)
    
    def refresh_state(self):
        self.contacts = self.request.user.contacts.all()
        self.users = self.get_non_contacts()


    class Meta:
        javascript_exclude = ("contacts", "users")