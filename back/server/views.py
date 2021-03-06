
# 路由分发

from . import app,api
from .resources.hellotest import Hello
from .resources.user import Add
from .resources.login import Login
from .resources.userInfoSave import UserInfoSave
from .resources.userInfoShow import UserInfoShow
from .resources.tokenCheck import TokenCheck
from .resources.Register import Register
from .resources.releaseSave import ReleaseSave
from .resources.showReleasePro import ShowReleasePro
from .resources.Recommend import Recommend
from .resources.showBase import ShowBase
from .resources.myProjectData import MyProjectData
from .resources.proPageQuery import ProPageQuery
from .resources.addApply import AddApply
from .resources.applyListShow import ApplyListShow
from .resources.applyUserList import ApplyUserList
from .resources.generatingOrder import GeneratingOrder
from .resources.haveInHandListShow import HaveInHandListShow
from .resources.showOrderData import ShowOrderData
from .resources.participantInfo import ParticipantInfo
from .resources.updateProgress import UpdateProgress
from .resources.checkProject import CheckProject
from .resources.increase import Increase













api.add_resource(Hello, '/')
api.add_resource(Add, '/user')
api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(TokenCheck, '/tokenCheck')
api.add_resource(UserInfoSave, '/userInfoSave')
api.add_resource(UserInfoShow, '/userInfoShow')
api.add_resource(ReleaseSave, '/releaseSave')
api.add_resource(ShowReleasePro, '/showReleasePro')
api.add_resource(Recommend, '/recommend')
api.add_resource(ShowBase, '/showBase')
api.add_resource(MyProjectData, '/myProjectData')
api.add_resource(ProPageQuery, '/proPageQuery')
api.add_resource(AddApply, '/addApply')
api.add_resource(ApplyListShow, '/applyListShow')
api.add_resource(ApplyUserList, '/applyUserList')
api.add_resource(GeneratingOrder, '/generatingOrder')
api.add_resource(HaveInHandListShow, '/haveInHandListShow')
api.add_resource(ShowOrderData, '/showOrderData')
api.add_resource(ParticipantInfo, '/participantInfo')
api.add_resource(UpdateProgress, '/updateProgress')
api.add_resource(CheckProject, '/checkProject')
api.add_resource(Increase, '/increase')











