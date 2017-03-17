/**
 * Created by a1exlism on 3/12/17.
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
} from 'react-native';

const Item = Picker.Item;

export default class Market extends Component {
	constructor(props) {
		super(props);
		this.state = {
			classShow1: '常用',
			classShow2: '分类',
			classShow3: '价格',
			usual: ['常用', '最近发布', '距离最近'],
			category: ['分类', '数码', '日用品', '家电', '服饰', '收藏', '其他'],
			values: ['价格', '由低到高', '由高到低'],
		}
	}
	
	genItems(items) {
		return (items.map((item, i) => {
				return (
					<Item key={i} label={item} value={i}/>
				);
			})
		)
	}
	
	//  todo: value 后端数据处理
	timeUpload() {
		let time = '13:10 ' + '1-5' + ' 发布';
		return time;
	}
	
	render() {
		return (
			<View style={styles.marketContainer}>
				{/* Picker Bars */}
				<View style={styles.pickerBars}>
					<Picker
						style={styles.pickerItem}
						selectedValue={this.state.classShow1}
						onValueChange={(val) => {
							this.setState({
								classShow1: val
							})
						}}
						mode="dropdown">
						{this.genItems(this.state.usual)}
					</Picker>
					
					<Picker
						style={styles.pickerItem}
						selectedValue={this.state.classShow2}
						onValueChange={(val) => {
							this.setState({
								classShow2: val
							})
						}}
						mode="dropdown">
						{this.genItems(this.state.category)}
					</Picker>
					<Picker
						style={styles.pickerItem}
						selectedValue={this.state.classShow3}
						onValueChange={(val) => {
							this.setState({
								classShow3: val
							})
						}}
						mode="dropdown">
						{this.genItems(this.state.values)}
					</Picker>
				</View>
				{/* Product List */}
				<View style={styles.goodsContainer}>
					<View style={styles.goodsRow}>
						<View style={styles.goodsRowTop}>
							{/* avatar */}
							<View>
								<Image
									style={styles.avatar}
									source={require('../images/avatars/avatar2.jpg')}
								/>
							</View>
							{/* name & time */}
							<View style={[styles.dirColumn]}>
								<Text style={[styles.username, styles.black]}>
									辉*明
								</Text>
								<Text style={[styles.uploadTime, styles.black]}>
									{this.timeUpload()}
								</Text>
							</View>
							{/* value */}
							<View style={styles.goodsValueView}>
								<Text style={styles.goodsValueText}>
									${"5500"}
								</Text>
							</View>
						</View>
						<View style={styles.goodsImgContainer}>
							<View style={styles.goodsImg}>
								<Image
									source={require('../images/userUpload/ip5-1.jpg')}
									style={[this.setSize(125)]}
								/>
							</View>
							<View style={styles.goodsImg}>
								<Image
									source={require('../images/userUpload/ip5-2.jpg')}
									style={[this.setSize(125)]}
								/>
							
							</View>
							<View style={styles.goodsImg}>
								<Image
									source={require('../images/userUpload/ip5-3.jpg')}
									style={[this.setSize(125)]}
								/>
							</View>
						</View>
						<View style={styles.goodsRowDescription}>
							<Text style={styles.black}>
								iPhone 5S 64G 全网通 杭州面交, 换过屏幕, 8成新
							</Text>
						</View>
						<View style={styles.goodsRowBottom}>
							<View style={styles.goodsFrom}>
								<Text>
									来自 {"杭州电子科技大学"}
								</Text>
							</View>
							<View style={styles.thumbsUp}>
								<Text style={styles.silver}>
									浏览: {"143"} 赞: {"3"}
								</Text>
							</View>
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
}

//  device height & width
const devWidth = Dimensions.get('window').width;
const devHeight = Dimensions.get('window').height;

const styles = StyleSheet.create({
	black: {
		color: 'black',
	},
	sliver: {
		color: 'silver',
	},
	dirRow: {
		flexDirection: 'row',
	},
	dirColumn: {
		flexDirection: 'column',
	},
	marketContainer: {
		flex: 1,
		flexDirection: 'column',
		alignItems: 'flex-start',
	},
	//  picker
	pickerBars: {
		flexDirection: 'row',
		justifyContent: 'space-between',
		borderBottomColor: '#E9E9E9',
		borderBottomWidth: 1,
	},
	pickerItem: {
		flex: 1,
	},
	//  goods single row
	goodsContainer: {
		flex: 1,
		alignSelf: 'stretch',
	},
	goodsRow: {
		flexDirection: 'column',
		height: 270,
		borderBottomColor: '#E9E9E9',
		borderBottomWidth: 1,
	},
	//  goods top
	goodsRowTop: {
		flex: 8,
		flexDirection: 'row',
		paddingTop: 10,
		paddingHorizontal: 8,
		alignItems: 'center',
	},
	avatar: {
		width: 60,
		height: 60,
		borderRadius: 50,
		marginRight: 10,
	},
	username: {
		fontWeight: "500",
	},
	uploadTime: {},
	goodsValueView: {
		position: 'absolute',
		right: 15,
		//  暂时解决这个问题
	},
	goodsValueText: {
		fontSize: 18,
		color: '#FF4522',
	},
	//  goods middle
	goodsImgContainer: {
		flexDirection: 'row',
		justifyContent: 'space-around',
		alignItems: 'center',
		flex: 16,
		height: 128,
	},
	goodsImg: {
		flexShrink: 1.2,
		marginHorizontal: 2,
	},
	goodsRowDescription: {
		marginLeft: 6,
	},
	//  goods bottom
	goodsRowBottom: {
		flex: 2,
		flexDirection: 'row',
	},
	goodsFrom: {
		marginLeft: 6,
	},
	thumbsUp: {
		position: 'absolute',
		right: 15,
	},
});
