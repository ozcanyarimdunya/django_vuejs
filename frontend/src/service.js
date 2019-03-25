import axios from "axios";
import store from './store';
import router from './router';

const apiUrl = {
  baseURL: process.env.NODE_ENV === 'production' ? '' : 'http://127.0.0.1:8000',
  admin: '/admin/',
  obtainToken: '/obtain-token/',
  refreshToken: '/refresh-token/',
  todo: {
    list: '/todo/list/',
    create: '/todo/create/',
    detail: '/todo/detail/',
    update: '/todo/update/',
    delete: '/todo/delete/',
    toggle: '/todo/toggle/',
  }
};


export const session = axios.create({
  baseURL: apiUrl.baseURL,
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
});

session.interceptors.response.use(response => response, error => {
  const {status} = error.response;
  if (status === 401) {/*Unauthorized*/
    store.dispatch('auth/logout')
      .then(() => {
        router.push({name: 'login'})
      });
  }
  return Promise.reject(error);
});

export default {
  login(username, password) {
    const url = apiUrl.obtainToken;
    return session.post(url, {username, password});
  },
  logout() {
    return new Promise((resolve, reject) => resolve());
  },
  getTodoList(params = {}) {
    const query = Object.keys(params).map(p => `${p}=${params[p]}`).join('&');
    const url = apiUrl.todo.list + '?' + query;
    return session.get(url);
  },
  createTodo(name) {
    const url = apiUrl.todo.create;
    return session.post(url, {name});
  },
  getTodo(id) {
    const url = apiUrl.todo.detail + id;
    return session.get(url);
  },
  updateTodo(id, name) {
    const url = apiUrl.todo.update + id;
    return session.put(url, {name});
  },
  deleteTodo(id) {
    const url = apiUrl.todo.delete + id;
    return session.delete(url);
  },
  toggleTodo(id) {
    const url = apiUrl.todo.toggle + id;
    return session.patch(url);
  },
};
