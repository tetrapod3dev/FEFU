package com.cloud.mapper;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import com.cloud.domain.CampaignDto;
import com.cloud.domain.CompanyDto;
import com.cloud.domain.OfficialAndPersonalDto;

@Mapper
public interface CampaignMapper {

	public List<CampaignDto> findAll(String campaignType, int pageNo, String type, String content, int startIndex, int perPageNum);
	public int findByCount(String campaignType, int pageNo, String type, String content);
	public List<String> findTagByNo(int no);
	public Map<String, Object> findDetail(int no, String type);
	public String findTypeByNo(int no);
	public int checkJoin(int no, String username);
	public int joinCampaign(int no, String username);
	public int leaveCampaign(int no, String username);
	public int insertCampaign(CampaignDto dto);
	public int insertCompany(CompanyDto dto);
	public int insertOfficialAndPersonal(OfficialAndPersonalDto dto);
	public int insertTag(List<String> tag);
	public int insertCampaignTag(List<String> tag, @Param("no") int no);
	public int updateCampaign(CampaignDto dto);
	public int deleteCampaign(int no);
}
