package com.cloud.util;

import java.util.HashMap;

import org.springframework.jdbc.support.JdbcUtils;

public class CamelHashMap extends HashMap{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	@SuppressWarnings("unchecked")
	@Override
	public Object put(Object key, Object value) {
		return super.put(JdbcUtils.convertUnderscoreNameToPropertyName((String)key), value);
	}
}
