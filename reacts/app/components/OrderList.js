'use strict';
import React, {Component} from 'react';
import {
	AppRegistry,
	Text,
	View,
	StyleSheet,
	Image,
} from 'react-native';
import {
	Tab,
	Tabs,
	Button,
	Content,
} from 'native-base';

import Market from './Market';
import Coupons from './Coupons';

export class ListExpress extends Component {
	render() {
		return (
			<View style={styles.listContainer}>
				<View style={styles.listRowContainer}>
					{/* LEFT */}
					<View style={styles.listRowLeft}>
						<View style={styles.rowLeftAvatar}>
							<Image
								source={require('../images/avatars/avatar1.jpg')}
								style={this.setImgCycle(60)}
							/>
						</View>
						<View style={styles.rowLeftName}>
							<Text>
								王*丽
							</Text>
						</View>
					</View>
					{/* MIDDLE */}
					<View style={styles.listRowMiddle}>
						<View style={styles.inlineRow}>
							<Image
								source={require('../images/orders/location@1x.png')}
								style={[this.setSize(15)]}
							/>
							<Text>
								北门菜鸟驿站
							</Text>
						</View>
						<View style={styles.inlineRow}>
							<Image
								source={require('../images/orders/package@1x.png')}
								style={[this.setSize(15)]}
							/>
							<Text>
								小件
							</Text>
						</View>
						<View style={styles.inlineRow}>
							<Image
								source={require('../images/orders/about@1x.png')}
								style={[this.setSize(15)]}
							/>
							<Text>
								4点前送到
							</Text>
						</View>
						<View style={styles.inlineRow}>
							<Image
								source={require('../images/orders/money@1x.png')}
								style={[this.setSize(15)]}
							/>
							<Text>
								$3
							</Text>
						</View>
					</View>
					{/* Right */}
					<View style={styles.listRowRight}>
						<View style={styles.rowRightTime}>
							<Text>
								16:10:30
							</Text>
						</View>
						<View style={styles.rowRightBtn}>
							<Button small success>
								<Text style={styles.colorWhite}>
									接单
								</Text>
							</Button>
						
						</View>
					</View>
				</View>
			</View>
		);
	}
	
	setSize(size) {
		return {
			width: size,
			height: size,
		}
	}
	
	setImgCycle(size) {
		return {
			width: size,
			height: size,
			borderRadius: 50,
		}
	}
}

export default class OrderList extends Component {
	render() {
		return (
			<Tabs initialPage={0}>
				<Tab heading="快递">
					<ListExpress/>
				</Tab>
				<Tab heading="代买">
					<ListExpress/>
				</Tab>
				<Tab heading="集市">
					<Market/>
				</Tab>
				<Tab heading="优惠券">
					{/* Content: react-native-keyboard-aware-scroll-view */}
					<View style={styles.couponContainer}>
						<Content>
							<Coupons/>
							<Coupons/>
							<Coupons/>
							<Coupons/>
							<Coupons/>
						</Content>
					</View>
				</Tab>
				<Tab heading="寻物">
					{/*Contents 5 */}
				</Tab>
			</Tabs>
		);
	}
	
}

const styles = StyleSheet.create({
	colorWhite: {
		color: 'white',
	},
	inlineRow: {
		flexDirection: 'row',
		flexWrap: 'wrap',
		alignItems: 'center',
	},
	listContainer: {
		flex: 1,
		flexDirection: 'column',
		paddingTop: 10,
	},
	listRowContainer: {
		flexDirection: 'row',
		borderBottomColor: '#CECECE',
		borderBottomWidth: 1,
		justifyContent: 'space-around',
		paddingVertical: 5,
	},
	listRowLeft: {
		paddingHorizontal: 0,
		justifyContent: 'center',
		alignItems: 'center',
		flex: 4,
	},
	listRowMiddle: {
		flex: 7,
	},
	listRowRight: {
		flex: 3,
		flexDirection: 'column',
		justifyContent: 'space-around',
	},
	rowRightTime: {
		//  all flex function are useless, why?
	},
	rowRightBtn: {},
	//  coupon container
	couponContainer: {
		flex:1,
		backgroundColor: '#f0f0f0',
		paddingTop: 12,
	}
});

AppRegistry.registerComponent('OrderList', () => OrderList);
