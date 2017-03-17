/**
 * Created by a1exlism on 3/13/17.
 */

import React, {
	Component
} from 'react';
import {
	View,
	StyleSheet,
	Picker,
	Image,
	Text,
	Dimensions,
	TouchableHighlight,
} from 'react-native';
import {
	ListItem
} from 'native-base';

export class Triangles extends Component {
	render() {
		return (
			<View style={styles.triangles}>
				{
					this.single('1234567890'.split(''))
				}
			</View>
		);
	}
	
	single(items) {
		return (
			items.map((items, i) => {
				return (
					<View style={styles.triangle} key={i}>
						<Text>i</Text>
					</View>
				)
			})
		)
	}
}
export default class Coupons extends Component {
	render() {
		return (
			
			<View style={styles.container}>
				{/* Single coupon */}
				<View style={styles.coupon}>
					{/* Left */}
					<Triangles/>
					<View style={styles.discount}>
						<Text style={styles.yuan}>
							¥
						</Text>
						<Text style={styles.count}>
							{10}
						</Text>
					</View>
					{/* Right */}
					<View style={styles.description}>
						<View style={styles.detail}>
							<Text >
								天鸿数码专营店无门槛优惠券
							</Text>
						</View>
						<View style={styles.timeExpired}>
							<Text>
								截止日期: {'00:00:00 4-15-2017'}
							</Text>
						</View>
						<TouchableHighlight
							activeOpacity={1}
							style={styles.btn}
						>
							<Text style={styles.btnText}>立即使用</Text>
						</TouchableHighlight>
					</View>
				</View>
			</View>
		);
	}
}

const {
	height,
	width
} = Dimensions.get('window');

const styles = StyleSheet.create({
	container: {
		flexDirection: 'column',
		flex: 1,
		paddingHorizontal: 10,
	},
	//  single container
	coupon: {
		
		height: height / 6,
		flexDirection: 'row',
		marginBottom: 10,
	},
	//  left
	triangles: {
		flexDirection: 'column',
	},
	triangle: {
		height: 0,
		width: 0,
		borderTopWidth: 5,
		borderTopColor: 'transparent',
		borderBottomWidth: 5,
		borderBottomColor: 'transparent',
		borderRightWidth: 2.5,
		borderRightColor: '#FF7D77',
	},
	discount: {
		flex: 3,
		flexDirection: 'row',
		justifyContent: 'center',
		alignItems: 'center',
		backgroundColor: '#FF7D77',
		height: 100
	},
	yuan: {
		color: 'white',
		fontSize: width / 16,
	},
	count: {
		color: 'white',
		fontSize: width / 10,
	},
	//  right
	description: {
		backgroundColor: 'white',
		height: 100,
		padding: 10,
		flex: 8,
		flexDirection: 'column',
		justifyContent: 'space-around',
		alignItems: 'flex-end',
	},
	detail: {},
	timeExpired: {},
	btn: {
		width: 70,
		height: 30,
		borderWidth: 1,
		borderColor: '#4d9fff',
		borderRadius: 8,
	},
	btnText: {
		fontSize: 15,
		margin: 2,
		textAlign: 'center',
		color: '#4d9fff',
	}
});