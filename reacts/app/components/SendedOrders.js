'use strict';
import React, { Component } from 'react';
import {
  AppRegistry,
  Text
} from 'react-native';

export default class MyOrders extends Component {
  render() {
    return (
      <Text>Page 3: MyOrders</Text>
    );
  }
}

AppRegistry.registerComponent('MyOrders', () => MyOrders);
