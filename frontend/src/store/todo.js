import {
  SET_TODOS,
  GET_TODOS_BEGIN,
  GET_TODOS_SUCCESS,
  GET_TODOS_FAILURE
} from '../consts';
import service from '../service';


const initialState = {
  todos: [],
  querying: false,
  error: false,
};

const getters = {};

const actions = {
  getTodoList({commit}, params) {
    commit(GET_TODOS_BEGIN);
    return service.getTodoList(params)
      .then(({data}) => commit(SET_TODOS, data))
      .then(() => commit(GET_TODOS_SUCCESS))
      .catch(() => commit(GET_TODOS_FAILURE))
  }
};

const mutations = {
  [GET_TODOS_BEGIN](state) {
    state.error = false;
    state.querying = true;
  },
  [GET_TODOS_FAILURE](state) {
    state.error = true;
    state.querying = false;
  },
  [GET_TODOS_SUCCESS](state) {
    state.error = false;
    state.querying = false;
  },
  [SET_TODOS](state, todos) {
    state.todos = todos;
  },
};

export default {
  namespaced: true,
  state: initialState,
  getters,
  actions,
  mutations,
};