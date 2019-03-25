<template>
  <div class="todos-wrapper">
    <a-table v-if="!error"
             :columns="columns"
             :rowKey="todo=>todo.id"
             :dataSource="todos"
             :loading="querying"
             bordered
             :pagination="{ pageSize: 5 }"
             @change="handleTableChange"
    >

      <template slot="title" slot-scope="currentPageData">
        <h3 style="text-align: center">Todos</h3>
      </template>
      <div slot="filterDropdown" slot-scope="{ setSelectedKeys, selectedKeys, confirm, clearFilters, column }"
           class='custom-filter-dropdown'>
        <a-input
                v-ant-ref="c => searchInput = c"
                :placeholder="`Search ${column.dataIndex}`"
                :value="selectedKeys[0]"
                @change="e => setSelectedKeys(e.target.value ? [e.target.value] : [])"
                @pressEnter="() => handleSearch(selectedKeys, confirm)"
                style="width: 188px; margin-bottom: 8px; display: block;"
        />
        <a-button
                type='primary'
                @click="() => handleSearch(selectedKeys, confirm)"
                icon="search"
                size="small"
                style="width: 90px; margin-right: 8px"
        >Search
        </a-button>
        <a-button
                @click="() => handleReset(clearFilters)"
                size="small"
                style="width: 90px"
        >Reset
        </a-button>
      </div>
      <a-icon slot="filterIcon" slot-scope="filtered" type='search'
              :style="{ color: filtered ? '#108ee9' : undefined }"/>
      <template slot="customRender" slot-scope="text">
                <span v-if="searchText">
                    <template
                            v-for="(fragment, i) in text.toString().split(new RegExp(`(?<=${searchText})|(?=${searchText})`, 'i'))">
                      <mark v-if="fragment.toLowerCase() === searchText.toLowerCase()" :key="i"
                            class="highlight">{{fragment}}</mark>
                      <template v-else>{{fragment}}</template>
                    </template>
                </span>
        <template v-else>{{text}}</template>
      </template>
    </a-table>
  </div>
</template>
<script>
  import {mapState, mapActions} from 'vuex';

  export default {
    name: 'Todos',
    data() {
      return {
        searchText: '',
        searchInput: null,
        columns: [
          {
            title: 'Name',
            dataIndex: 'name',
            key: 'name',
            sorter: true,
            scopedSlots: {
              filterDropdown: 'filterDropdown',
              filterIcon: 'filterIcon',
              customRender: 'customRender',
            },
            onFilter: (value, todo) => todo.name.toLowerCase().includes(value.toLowerCase()),
            onFilterDropdownVisibleChange: (visible) => {
              if (visible) {
                setTimeout(() => {
                  this.searchInput.focus()
                }, 0)
              }
            },
          }, {
            title: 'Completed',
            dataIndex: 'completed',
            key: 'completed',
            sorter: true,
          }, {
            title: 'Created',
            dataIndex: 'created',
            key: 'created',
            sorter: true,
          }, {
            title: 'Updated',
            dataIndex: 'updated',
            key: 'updated',
            sorter: true,
          },
        ]
      }
    },
    mounted() {
      this.getTodoList();
    },
    computed: {
      ...mapState('todo', ['todos', 'querying', 'error']),
    },
    methods: {
      ...mapActions('todo', ['getTodoList']),

      handleTableChange(pagination, filters, sorter) {
        const pre = sorter.order === 'ascend' ? `-` : '';
        const ordering = pre + sorter.field;
        const params = {ordering};
        this.getTodoList(params)
      },
      handleSearch(selectedKeys, confirm) {
        confirm();
        this.searchText = selectedKeys[0]
      },
      handleReset(clearFilters) {
        clearFilters();
        this.searchText = ''
      },
    },
  }
</script>
<style scoped lang="scss">
  .todos-wrapper {
    padding-top: 0;
  }

  .custom-filter-dropdown {
    padding: 8px;
    border-radius: 4px;
    background: #fff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .15);
  }

  .highlight {
    background-color: rgb(255, 192, 105);
    padding: 0;
  }
</style>