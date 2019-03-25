import Vue from 'vue'
import Router from 'vue-router'
import store from './store';

const requireAuthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (!store.getters['auth/isAuthenticated']) {
        next('/login');
      } else {
        next();
      }
    });
};

const requireUnauthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (store.getters['auth/isAuthenticated']) {
        next('/home');
      } else {
        next();
      }
    });
};

const redirectLogout = (to, from, next) => {
  store.dispatch('auth/logout')
    .then(() => next('/login'));
};

Vue.use(Router);


export default new Router({
  saveScrollPosition: true,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/Home'),
      beforeEnter: requireAuthenticated,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('./views/About'),
      beforeEnter: requireAuthenticated,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login'),
      beforeEnter: requireUnauthenticated,
    },
    {
      path: '/logout',
      name: 'logout',
      beforeEnter: redirectLogout,
    },
    {
      path: '*',
      name: 'lost',
      component: () => import('./views/Lost'),
    },
  ]
})
