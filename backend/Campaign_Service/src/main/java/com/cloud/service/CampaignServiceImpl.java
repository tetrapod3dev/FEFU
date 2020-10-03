package com.cloud.service;

import java.sql.Date;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.cloud.domain.CampaignDto;
import com.cloud.domain.CompanyDto;
import com.cloud.domain.OfficialAndPersonalDto;
import com.cloud.mapper.CampaignMapper;

@Service
public class CampaignServiceImpl implements CampaignService {

	private static final Logger logger = LoggerFactory.getLogger(CampaignServiceImpl.class);

	@Autowired
	private CampaignMapper campaignMapper;

	@Override
	public List<CampaignDto> findAll(String campaignType, int pageNo, String type, String content, int startIndex,
			int perPageNum) {
		type = type.trim();
		content = content.trim();
		return campaignMapper.findAll(campaignType, pageNo, type, content, startIndex, perPageNum);
	}

	@Override
	public int findByCount(String campaignType, int pageNo, String type, String content) {
		type = type.trim();
		content = content.trim();
		return campaignMapper.findByCount(campaignType, pageNo, type, content);
	}

	@Override
	public List<String> findTagByNo(int no) {
		return campaignMapper.findTagByNo(no);
	}

	@Override
	public Map<String, Object> findDetail(int no) {
		Map<String, Object> list = new HashMap<>();

		String type = campaignMapper.findTypeByNo(no);
		Map<String, Object> map = campaignMapper.findDetail(no, type.trim());

		CampaignDto campaign = setCampaign(map);
		campaign.setNo(no);
		campaign.setTag(findTagByNo(no));
		list.put("campaign", campaign);
		if (type.equals("company")) {
			list.put(type, setCompany(map));
		} else if (type.equals("official") || type.equals("personal")) {
			list.put(type, setOAP(map));
		}
		
		int total = campaignMapper.findByJoinCount(no);
		list.put("currentMember", total);

		return list;
	}

	@SuppressWarnings({ "unchecked" })
	@Override
	@Transactional
	public int insertCampaign(Map<String, Object> data) {
		CampaignDto campaign = null;
		CompanyDto company = null;
		OfficialAndPersonalDto oap = null;
		Map<String, Object> map = null;

		for (String key : data.keySet()) {
			if (key.equals("campaign")) {
				map = (Map<String, Object>) data.get(key);
				campaign = setCampaign(map);
			} else if (key.equals("tag")) {
				campaign.setTag((List<String>) data.get(key));
			} else if (key.equals("company")) {
				map = (Map<String, Object>) data.get(key);
				company = setCompany(map);
			} else if (key.equals("official") || key.equals("personal")) {
				map = (Map<String, Object>) data.get(key);
				oap = setOAP(map);
			}
		}

		int res = campaignMapper.insertCampaign(campaign);
		int no = campaign.getNo();
		res += campaignMapper.insertTag(campaign.getTag());
		res += campaignMapper.insertCampaignTag(campaign.getTag(), no);
		if (campaign.getType().equals("company")) {
			company.setNo(no);
			res += campaignMapper.insertCompany(company);
		} else if (campaign.getType().equals("official") || campaign.getType().equals("personal")) {
			oap.setNo(no);
			res += campaignMapper.insertOfficialAndPersonal(oap);
		}

		return res;
	}
	
	@Override
	public List<CampaignDto> findByJoinCampaign(String username) {
		return campaignMapper.findByJoinCampaign(username);
	}
	
	@Override
	public List<CampaignDto> findByRegistCampaign(String username) {
		return campaignMapper.findByRegistCampaign(username);
	}

	@Override
	public int updateCampaign(CampaignDto dto) {
		return campaignMapper.updateCampaign(dto);
	}

	@Override
	public int deleteCampaign(int no) {
		return campaignMapper.deleteCampaign(no);
	}

	@Override
	public int checkJoin(int no, String username) {
		return campaignMapper.checkJoin(no, username);
	}

	@Override
	public int joinCampaign(int no, String username) {
		return campaignMapper.joinCampaign(no, username);
	}

	@Override
	public int leaveCampaign(int no, String username) {
		return campaignMapper.leaveCampaign(no, username);
	}

	private CampaignDto setCampaign(Map<String, Object> map) {
		CampaignDto campaign = new CampaignDto();
		SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
		try {
			campaign.setTitle((String) map.get("title"));
			campaign.setContent((String) map.get("content"));
			if (map.get("endDate") instanceof String) {
				campaign.setEndDate(format.parse((String) map.get("endDate")));
				campaign.setStartDate(format.parse((String) map.get("startDate")));
			} else {
				campaign.setEndDate((Date) map.get("endDate"));
				campaign.setStartDate((Date) map.get("startDate"));
			}
			campaign.setType((String) map.get("type"));
			campaign.setWriter((String) map.get("writer"));
			campaign.setPhoto((String) map.get("photo"));
		} catch (ParseException e) {
			logger.info("날짜 포맷 에러");
		}
		return campaign;
	}

	private CompanyDto setCompany(Map<String, Object> map) {
		CompanyDto company = new CompanyDto();
		company.setCampaignLink((String) map.get("campaignLink"));
		company.setCompanyName((String) map.get("companyName"));
		return company;
	}

	private OfficialAndPersonalDto setOAP(Map<String, Object> map) {
		OfficialAndPersonalDto oap = new OfficialAndPersonalDto();
		oap.setAuthEndTime((String) map.get("authEndTime"));
		oap.setAuthStartTime((String) map.get("authStartTime"));
		oap.setAuthProcess((String) map.get("authProcess"));
		oap.setMission((String) map.get("mission"));
		oap.setHeadcount((int) map.get("headcount"));
		oap.setRequirement((String) map.get("requirement"));
		return oap;
	}
}
