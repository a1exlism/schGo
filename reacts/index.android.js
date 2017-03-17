/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, {Component} from 'react';
import {
	AppRegistry,
	StyleSheet,
	View,
	Image,
} from 'react-native';
import {
	Container,
	Header,
	Body,
	Title,
	Tab,
	Tabs,
	Text,
	Footer,
	FooterTab,
	Button,
} from 'native-base';

import OrderList from './app/components/OrderList';
import ReceivedOrders from './app/components/ReceivedOrders';
import NewOrder from './app/components/NewOrder';
import SendedOrders from './app/components/SendedOrders';
import User from './app/components/User';

export default class schoolgo extends Component {
	render() {
		return (
			<Container>
				<Header>
					<Body>
					<Title>Title</Title>
					{/* todo: title should change dynamically with the change of footer bar */}
					</Body>
				</Header>
				<OrderList/>
				
				<Footer>
					<FooterTab>
						<Button>
							
							<Image
								source={require('./app/images/footer/invert/order_list.png')}
								style={this.setSize(25)}
							/>
							<Text>
								任务列表
							</Text>
						</Button>
						<Button>
							<Image
								source={require('./app/images/footer/invert/received_orders.png')}
								style={this.setSize(23)}
							/>
							<Text>
								我的接单
							</Text>
						</Button>
						<Button>
							<Image
								source={require('./app/images/footer/invert/plus.png')}
								style={this.setSize(35)}
							/>
							<Text>
								发布
							</Text>
						</Button>
						<Button>
							<Image
								source={require('./app/images/footer/invert/my_orders.png')}
								style={this.setSize(27)}
							/>
							<Text>
								我的订单
							</Text>
						</Button>
						<Button>
							<Image
								source={require('./app/images/footer/invert/user.png')}
								style={this.setSize(25)}
							/>
							<Text>
								我的
							</Text>
						</Button>
					</FooterTab>
				</Footer>
			
			</Container>
		);
	}
	
	setSize(size) {
		return ({
			width: size,
			height: size
		})
	}
}


const styles = StyleSheet.create({});

AppRegistry.registerComponent('schoolgo', () => schoolgo);
