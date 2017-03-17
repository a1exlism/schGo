'use strict';
import React, { Component } from 'react';
import {
  AppRegistry,
  Text
} from 'react-native';

export default class User extends Component {
  render() {
    return (
      <Text>User</Text>
    );
  }
}

AppRegistry.registerComponent('User', () => User);
