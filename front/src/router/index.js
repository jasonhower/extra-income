import Vue from 'vue'
import Router from 'vue-router'
const Index = () => import('@/pages/Index')
const Projects = () => import('@/pages/Projects')
const Expert = () => import('@/pages/Expert')
const UserInfo = () => import('@/pages/UserInfo')
const ShowUserInfo = () => import('@/pages/ShowUserInfo')
const ReleasePro = () => import('@/pages/ReleasePro')
const ShowReleasePro = () => import('@/pages/ShowReleasePro')
const ShowMoreRelease = () => import('@/pages/ShowMoreRelease')
const ProjectOrder = () => import('@/pages/ProjectOrder')







Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/myProjects',
      name: 'projects',
      component: Projects
    },
    {
      path: '/expert',
      name: 'expert',
      component: Expert
    },
    {
      path: '/userInfo',
      name: 'userInfo',
      component: UserInfo
    },
    {
      path: '/showUserInfo/:id',
      name: 'showUserInfo',
      component: ShowUserInfo,
      props: true,
    },
    {
      path: '/releasePro',
      name: 'releasePro',
      component: ReleasePro
    },
    {
      path: '/showReleasePro/:id',
      name: 'showReleasePro',
      component: ShowReleasePro,
      props: true,
    },
    {
      path: '/showMoreRelease',
      name: 'showMoreRelease',
      component: ShowMoreRelease
    },
    {
      path: '/projectOrder/:id',
      name: 'projectOrder',
      component: ProjectOrder,
      props: true,
    }
  ]
})
