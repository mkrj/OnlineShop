import xadmin

from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(object):
    list_display = ['user', 'goods', 'goods']


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', 'message', 'message_type']


class UserAddressAdmin(object):
    list_display = ['signer_name', 'signer_mobile', 'district', 'address']


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
