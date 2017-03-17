'use strict';
import React, { Component } from 'react';
import {
  AppRegistry,
  Text
} from 'react-native';

export default class NewOrders extends Component {
  render() {
    return (
      <Text>Page 2: NewOrders</Text>
    );
  }
}

AppRegistry.registerComponent('NewOrders', () => NewOrders);
